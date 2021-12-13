const productos = document.getElementById("lista-productos");
const totalCarrito = document.getElementById('total-carrito');
const btnVaciarCarrito = document.getElementById('vaciar-carrito');
const btnPagar = document.getElementById('pagar');
const cantCarrito = document.getElementById('cant-productos');


let pedido=[];


function agregarProducto(id){
    console.log(id);
    if(pedido.includes(id) === false){
        pedido.push(id);
    }
    console.log(JSON.stringify(pedido));
    localStorage.setItem("pedido", JSON.stringify(pedido) );
    window.location.reload();
}

function cargarEventos(){
    productos.addEventListener("click",(e) =>{
        if(e.target.classList.contains("btn")){
            agregarProducto(e.target.id);   
        }
    });
}

function cargarLocalStorage(){
    if(localStorage.getItem('pedido')){ 
        pedido = localStorage.getItem('pedido')
        console.log(pedido);
        pedido = JSON.parse(pedido);
    } 
    cantCarrito.innerHTML = pedido.length;
    listaCarrito(pedido);
}

function listaCarrito(pedido){
    const cant_productos = document.getElementById('cantidad-productos');
    cant_productos.innerHTML = 'Productos en el carrito: ' + pedido.length + '';
    const productos_carrito = document.getElementById("lista-carrito");
    const forminputs = document.getElementById('inputs');

    let totalPedido = 0;
    if(pedido.length > 0){
        pedido.forEach(id => {
            let li = document.createElement('li');
            
            JSON.parse(productos_json).forEach(producto => {
                if(producto.id == id){
                    li.textContent = producto.nombre + '  $' + producto.precio;
                    productos_carrito.appendChild(li);
                    totalPedido += producto.precio;

                    let input = document.createElement('input');
                    input.type = 'text';
                    input.value = producto.id;
                    input.name = producto.id;
                    forminputs.appendChild(input);
                }
            })
        });
    }else{
        console.log('pedido vacio');
        btnVaciarCarrito.style.visibility = 'hidden';
        btnPagar.style.visibility = 'hidden';
    }

    totalCarrito.innerHTML += ' ' + totalPedido
    console.log(pedido);
    console.log(JSON.parse(productos_json)); 
}

function vaciarCarrito(){
    localStorage.removeItem('pedido');
    window.location.reload();
}

cargarEventos();
