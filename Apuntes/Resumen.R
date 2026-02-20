### Apuntes de R

## Bases de datos
# Crear vetores
x = c("a", "b", "...")

# Crear una secuencia linea
seq(first, last, by=steps)

# Crear tabla
tabla = data.frame(x1, x2, xn)

str(tabla) # Imrpime la tabla completa
summary(tabla) # Imprime un resumen con los datos relevantes

tabla[c(fil1, fil2), c(col1, col2)] # Podemos pedir filas y columnas en particular

tabla["col"] # Podemos pedir una columna de la tabla

tabla[tabla["col"]=={criterio},] # Filter (recordar la ,)

## Medidas descriptivas
mean(x) # Calcula la media de un vector
var(x) # Varianza de x
sd(x) # standart deviation de x
median(x) # Mediana
quantile(x, p) # El percentil p% de x
min(x) # Valor mínimo
max(x) # Valor máximo
range(x) # Min y max
sort(x) # Ordena x de menor a mayor
sort(x)[m] # Obtiene el m menor valor
IQR(x) 
unique(x) # Retorna todos los valores únicos del vector
table(x) # Retorna una tabla con los valores del vector
# Requiere library(modeest)
mlv(x) # Moda
# Requiere library(moments)
skewness(x)
kurtosis(x)-3 # Recordar -3

### Representación de datos

plot(x, y) # Hace un gráfico con los puntos de los vectores x e y
# xlab="", ylab="" Labelea los ejes x e y
# main="" Titulo del gráfico
# col="", lwd="", lty="" color, line widht, line type

boxplot(x)
# Horizontal= (bool) indica si la caja estará parada o acostada

hist(x) # Histograma

barplot(x) # Gráfico de barras

## Bases de datos 2
library(dyplr) # Recordar descargarlo en Tools > Install packages

# Recordar q no sobreescriben los datos, por lo q hay q asignarlos a una nueva variable

filter(tabla, {criterio1}, {criterio2}, {criterion}) # Filtra, pero más bonito

arrange(tabla, col) # Sortea la tabla según la columna
# Se puede sortear al revés con desc(col)

select(tabla, col1, col2) # Da un subconjunto de la tabla con las columnas

rename(tabla, nombre_nuevo=nombre_viejo) # Renombra una columna

mutate(tabla, col_nueva={funcion}) # Añade una nueva columna en función de las existentes

transmute(tabla,  col_nueva={funcion}) # Igual eal mutate, pero retorna la col en vez de añadirla a la tabla

sumarise(tabla, cols) # Tira una tabla de resumen con los valores que le pidamos en las columnas

### Modelos de probabilidad
d____(x) # Entrega la probabilidad (o densidad) en un punto
p____(q) # Calcula la probabilidad acumulada
q____(p) # Calcula el quantile q
r____(n) # Genera n vars aleatorias

_exp(x, rate=) # rate = nu
_pois(x, lambda=)
_unif(x, min=, max=)
_norm(x, mean=, sd=) # Media y standart deviation
_lnorm(x, meanlog=, sdlog=)
_gamma(x, shape=, rate=)
_binom(x, size=, prob=)

##### Lab 2

# Funciones
funcion = function(x, y){
    cuerpo = ifelse(
        cond1, valor,
        cond2, valor2, 
        valor_else
    )
    return(cuerpo)
}

prop.table(tabla) # Retorna una tabla de proporciones
# margin=1 hace que calcule las proporciones para cada fila (Probabilidad de fila dada la columna)
# margin=2 hace que calcule las proporciones para cada columna (Probabilidad de columna dada la fila)

rowSums(tabla) # Retorna la suma de todos los valores de las filas
colSums(tabla) # Retorna la suma de todos los valores de las columnas

# La funcion de probabilidad conjunta se obtiene multiplicando ambas distribuciones usando function{}
# La probabilidad condicional se puede calcular con el teorema de Bayes

cov(var1, var2) # Obtiene la covarianza entre dos variables
# Para la correlacion hay que usar la formula

_mvnorm(lower=, upper=, mean=, sigma=) # Para la normal bivariada hay que usar library(mvtnorm)
# Lower es un vector de cotas inferiores de las variables, y upper las superiores
# mean es un vector con las medias, sigma es una matriz de varianza (ver formula)
# La matriz de varianza se arma con matrix(c(, , , , ), 2,2)

lm(var1 ~ var2) # Obtiene el intercepto y pendiente de la regresion lineal de los datos
# Si la regresion se guarda como variable, se puede acceder a los atributos con model$coefficients o coef

### En R se puede usar el teorema del limite central (no hay comando, usar formula)
# Ajuste por continuidad: sumar el 50% del salto de la probabilidad pedida (ej. 0.56 => 0.565)

### Para valores extremos seguir las formulas

fitdist(data, distr=, method=, fix.arg=list(param=value)) # Requiere library(fitdistrplus)
# distr es la distribucion, fix.arg permite ingresar una lista con los parametros ya conocios
# method puede ser "mme" (metodo de los momentos), o "mle" (maxima verosimilitud)

### Test de hipotesis
## media y sigma conocido
z.test(data, mu=mu_0, sd=sigma, alternative=) # Requiere library(TeachingDemos)
# alternative puede ser "two.sided" (!=), "less" (>), "greater" (<)

## media conocida, sigma desconocido
t.test(data, mu=mu_0, alternative=)

## sigma conocido, media desconocida
sigma.test(Var, sigma=sigma_0, alternative=) # Requiere library(TeachingDemos)

## test de proporciones
prop.test(exitos, intentos, p=p_0, alternative=, correct=FALSE) # Para bernoullis

## test KS
ks.test(x=data, y="p____", param1=param_1, param2=param_2) # Requiere estimar los parametros con fitdistr()