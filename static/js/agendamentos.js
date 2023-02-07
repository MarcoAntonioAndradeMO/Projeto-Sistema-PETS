function cadastrar() {
    var data = {
        "paciente": document.getElementById("paciente").value,
        "veterinario": document.getElementById("veterinario").value,
        "data_consulta": document.getElementById("data_consulta").value
    };
    let headers = {
        withCredentials: true,
        xsrfHeaderName: "X-CSRFTOKEN",
        xsrfCookieName : "csrftoken",
        headers: {
            "Content-Type": "application/json"
        }
    }
    axios.post('/api/agendamentos/', data, headers)
      .then(function (response) {
        alert("Agendamento inserido");
        document.getElementById("paciente").value = "";
        document.getElementById("veterinario").value = "";
        document.getElementById("data_consulta").value = "";
      })
      .catch(function (error) {
        console.error(error);
    });
}

function listar() {
  axios.get('/api/veterinarios/')
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.error(error);
  })
  .then(function () {
  });
}