
const axios = require('axios').default;


let form = document.getElementById('call-to-action');

form.addEventListener('submit', function(event) {
    event.preventDefault()

    let data = new FormData();

    data.append("title", document.getElementById('title').value)
    data.append("note", document.getElementById('note').value)
    data.append("csrfmiddlewaretoken", '{{csrf_token}}')

    axios.post('save_substitute/', data)
     .then(res => alert("Form Submitted"))
     .catch(errors => console.log(errors))

})
