document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".ver-detalles").forEach(function (elemento) {
        elemento.addEventListener("click", function (e) {
            e.preventDefault();
            let productoId = this.getAttribute("data-id");

            fetch(`/producto/detalle/${productoId}/`)
                .then(response => response.json())
                .then(data => {
                    let modalBody = document.getElementById("productoDetalle");
                    modalBody.innerHTML = `
                        <div class="row">
                            <div class="col-md-6">
                                <img src="${data.imagen}" class="img-fluid" alt="${data.nombre}">
                            </div>
                            <div class="col-md-6">
                                <h3>${data.nombre}</h3>
                                <p><strong>Descripción:</strong> ${data.descripcion}</p>
                                <p><strong>Precio:</strong> Q${data.precio}</p>
                                <p><strong>Categoría:</strong> ${data.categoria}</p>
                                <a href="/agregar-al-carrito/${productoId}/" class="btn btn-success">
                                    <i class="fas fa-cart-plus"></i> Añadir al carrito
                                </a>
                            </div>
                        </div>
                    `;
                    let productoModal = new bootstrap.Modal(document.getElementById("productoModal"));
                    productoModal.show();
                })
                .catch(error => console.error("Error al obtener los datos:", error));
        });
    });
});