function cadastrar() {
    var data = {
        "cpf": document.getElementById("cpf").value,
        "nome_do_dono": document.getElementById("nome_do_dono").value,
        "nome_do_animal": document.getElementById("nome_do_animal").value,
    };
    let headers = {
        withCredentials: true,
        xsrfHeaderName: "X-CSRFTOKEN",
        xsrfCookieName : "csrftoken",
        headers: {
            "Content-Type": "application/json"
        }
    }
    axios.post('/api/pacientes/', data, headers)
      .then(function (response) {
        alert("Paciente inserido");
        document.getElementById("cpf").value = "";
        document.getElementById("nome_do_dono").value = "";
        document.getElementById("nome_do_animal").value = "";
      })
      .catch(function (error) {
        console.error(error);
    });
}

function consulta() {
    var cpf = document.getElementById("cpf").value;
    axios.get('/api/pacientes?cpf=' + cpf)
    .then(function (response) {
        let pacientes = "";
        for (p in response.data) {
            let paciente = response.data[p];
            var cpf_paciente = "<td>" + paciente.cpf + "</td>"
            var nome_paciente = "<td>" + paciente.nome_do_dono + "</td>"
            var nome_do_animal = "<td>" + paciente.nome_do_animal + "</td>"
            var historico = '<td><button class="btn btn-primary" onclick="paginaPaciente(' + paciente.cpf + ')">Página do Paciente</button></td>'
            pacientes = pacientes + "<tr> " + cpf_paciente + nome_paciente + nome_do_animal + historico + "</tr>"
        }
        document.getElementById("lista").innerHTML = pacientes;
    })
    .catch(function (error) {
        console.error(error);
    })
    .then(function () {
    });
}

function paginaPaciente(cpf) {
    window.location.href = '/pacientes/' + cpf + '/';
}

function consultaAgendamentos(cpf) {
  axios.get('/api/agendamentos/?paciente=' + cpf)
  .then(function (response) {
    console.log(response.data);
    let obj_list = "";
    let data_obj = response.data[0];
    var veterinario = "<td>" + data_obj.veterinario.nome + "</td>"
    var especialidade = "<td>" + data_obj.veterinario.especialidade + "</td>"
    var data_consulta = "<td>" + data_obj.data_consulta + "</td>"
    obj_list = obj_list + "<tr> " + data_consulta + veterinario + especialidade + "</tr>"
    document.getElementById("lista").innerHTML = obj_list;
    document.getElementById("nome_dono").innerHTML = data_obj.paciente.nome_do_dono;
    document.getElementById("cpf_dono").innerHTML = data_obj.paciente.cpf;
  })
  .catch(function (error) {
    console.error(error);
  })
  .then(function () {
  });
}