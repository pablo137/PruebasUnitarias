// JavaScript (con jQuery)

$(document).ready(function() {
    // Evento de clic en el botón de editar
    $('.btn-editar').on('click', function() {
      let productoId = $(this).data('producto-id');
      // Realizar la solicitud Ajax para obtener el formulario de edición
      $.ajax({
        url: "{% url 'editar_producto' %}" + productoId + '/',
        type: 'GET',
        success: function(response) {
          // Insertar el formulario de edición en algún contenedor en la página actual
          $('#formulario-edicion').html(response);
        },
        error: function() {
          alert('Ocurrió un error al cargar el formulario de edición.');
        }
      });
    });
  
    // Evento de clic en el botón de eliminar
    $('.btn-eliminar').on('click', function() {
      let productoId = $(this).data('producto-id');
      // Realizar la solicitud Ajax para eliminar el producto
      $.ajax({
        url: "{% url 'eliminar_producto' %}" + productoId + '/',
        type: 'POST',
        data: {
          csrfmiddlewaretoken: '{{ csrf_token }}' // Asegúrate de incluir el token CSRF en la solicitud POST
        },
        success: function(response) {
          // Realizar alguna acción después de eliminar el producto, como actualizar la tabla de productos
          alert('El producto ha sido eliminado correctamente.');
        },
        error: function() {
          alert('Ocurrió un error al eliminar el producto.');
        }
      });
    });
  });