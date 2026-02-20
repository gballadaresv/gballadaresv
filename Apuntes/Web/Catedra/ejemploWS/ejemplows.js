const socket = new WebSocket('ws://192.46.217.146:3000/ws');

socket.onopen = () => {
  console.log('Atención clase, conexión WebSocket abierta!');
};

/*socket.onmessage = async event => {
    console.log(event.data);
	console.log(event.data.text());
	texto = await event.data.text(); // convierte Blob a texto
    document.getElementById('respuesta').innerText = 'Respuesta: ' + texto;
};*/
socket.onmessage = async event => {
    console.log('event.data:', event.data);
    console.log('typeof:', typeof event.data);
    console.log('instanceof Blob:', event.data instanceof Blob);

    let texto;
    if (event.data instanceof Blob) {
        texto = await event.data.text();
    } else {
        texto = event.data;
    }

    document.getElementById('respuesta').innerText = 'Respuesta: ' + texto;
};

document.getElementById('enviar').addEventListener('click', () => {
  const msg = document.getElementById('mensaje').value;
	console.log(msg);
  socket.send(msg);
});