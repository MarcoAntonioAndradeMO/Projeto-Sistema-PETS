function cadastrar() {
    var data = {
        "cmrv": document.getElementById("cmrv").value,
        "nome": document.getElementById("nome").value,
        "especialidade": document.getElementById("especialidade").value
    };
    let headers = {
        withCredentials: true,
        xsrfHeaderName: "X-CSRFTOKEN",
        xsrfCookieName : "csrftoken",
        headers: {
            "Content-Type": "application/json"
        }
    }
    axios.post('/api/veterinarios/', data, headers)
      .then(function (response) {
        alert("Veterinario inserido");
        document.getElementById("cmrv").value = "";
        document.getElementById("nome").value = "";
        document.getElementById("especialidade").value = "";
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