// Estado simple en memoria (NO usar nunca localStorage para JWT en produccion)

const state = { jwt: null };
const $ = (id) => document.getElementById(id); //un modesto alias para evitar escribir tanto
const origin = location.origin; 

//Esta fncion da un on/off a algun estilo dado por la clase que cambia según el caso
function setPill(el, text, type = null) {
  el.textContent = text;
  el.className = "pill" + (type ? " " + type : "");
}

function show(obj, el) {
  el.textContent = typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
}

function setBusy(button, busy) {
  button.disabled = !!busy;
  if (busy) { button.dataset.old = button.textContent; button.textContent = "Trabajando…"; }
  else if (button.dataset.old) { button.textContent = button.dataset.old; }
}

function refreshBadges() {
  setPill($("pillSess"), "Sesión: desconocida");
  setPill($("pillJwt"), state.jwt ? "JWT: presente" : "JWT: vacío", state.jwt ? "ok" : null);
}
refreshBadges();

// Acciones que son gatillados por los botones

async function login() {
  let email = $("email").value.trim();
  let password = $("password").value;
  let btn = $("btnLogin");

  setBusy(btn, true);
  try {
    const res = await fetch(origin + "/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include", // cookie 'sess'
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok) throw new Error(data.error || res.statusText);
    state.jwt = data.jwt || null;
    show(data, $("outLogin"));
    setPill($("pillJwt"), state.jwt ? "JWT: presente" : "JWT: vacío", state.jwt ? "ok" : "bad");
    setPill($("pillSess"), "Sesión: establecida (cookie)", "ok");
  } catch (err) {
    show({ error: err.message }, $("outLogin"));
    setPill($("pillSess"), "Sesión: fallo login", "bad");
    setPill($("pillJwt"), "JWT: vacío", "bad");
  } finally {
    setBusy(btn, false);
  }
}

async function me() {
  let btn = $("btnMe");
  setBusy(btn, true);

  try {
	  //Acá, otro fetchj
    const res = await fetch(origin + "/me", {
      method: "GET",
      credentials: "include" // envía cookie de sesión
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || res.statusText);
    show(data, $("outMe"));
    setPill($("pillSess"), "Sesión: activa (cookie)", "ok");
  } catch (err) {
    show({ error: err.message }, $("outMe"));
    setPill($("pillSess"), "Sesión: no activa", "bad");
  } finally {
    setBusy(btn, false);
  }
}

async function gameCurrent() {
  let btn = $("btnGame");
  setBusy(btn, true);

  try {
    if (!state.jwt) throw new Error("No hay JWT. Haz login primero.");
    const res = await fetch(origin + "/api/game/current", {
      headers: { "Authorization": "Bearer " + state.jwt }
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || res.statusText);
    show(data, $("outGame"));
  } catch (err) {
    show({ error: err.message }, $("outGame"));
  } finally {
    setBusy(btn, false);
  }
}

async function logout() {
  const btn = $("btnLogout");
  setBusy(btn, true);
  try {
    const res = await fetch(origin + "/logout", {
      method: "POST",
      credentials: "include"
    });
    const data = await res.json().catch(()=>({}));
    show(data || { message: "Logout enviado" }, $("outMe"));
    state.jwt = null;
    setPill($("pillJwt"), "JWT: vacío");
    setPill($("pillSess"), res.ok ? "Sesión: cerrada" : "Sesión: no activa", res.ok ? "ok" : "bad");
  } catch (err) {
    show({ error: err.message }, $("outMe"));
  } finally {
    setBusy(btn, false);
  }
}

// Eventos "escuchados"

//asegurar que el DOM ya esté cargado antes de buscar los botones

window.addEventListener("DOMContentLoaded", () => {
  $("btnLogin").addEventListener("click", login);
  $("btnMe").addEventListener("click", me);
  $("btnGame").addEventListener("click", gameCurrent);
  $("btnLogout").addEventListener("click", logout);
});
