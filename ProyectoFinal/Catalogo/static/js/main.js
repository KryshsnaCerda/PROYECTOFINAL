$("#btn-ocultar").click(function(){
    $("fieldset").hide();

});

$("#btn-mostrar").click(function(){
    $("fieldset").show();

});

function getCurrentTime() {
    fetch('https://worldtimeapi.org/api/ip')
        .then(response => response.json())
        .then(data => {
            const datetime = new Date(data.datetime);
            const options = { hour: 'numeric', minute: 'numeric'};
            const formattedTime = datetime.toLocaleString('es-ES', options);
            document.getElementById('current-time').textContent = formattedTime;
        })
        .catch(error => {
            console.error('Error al obtener la hora:', error);
        });
}
getCurrentTime();
