$(document).ready(function(){
    $('.btn-registrar').click(function(e)
    {
        e.preventDefault();

        codigo = document.getElementById('codigo de circulación').value;
        empresa= document.getElementById('nombre empresa').value;
        actividad = document.getElementById('actividad').value;
        nombre = document.getElementById('nombre').value;
        apellido = document.getElementById(' apellido').value;
        dni = document.getElementById('dni').value;

        var url = window.location.href

        $.post(url, {codigo: codigo, empresa: empresa, actividad: actividad, nombre: nombre, apellido: apellido, dni: dni},
            function(data) {
                $('#div_image').html('<img src="data:image/png;base64,' + data + '" />');      
                    
            }
        );
 
    });
});