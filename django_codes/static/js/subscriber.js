let subscriberForm = document.getElementById('subscribe-form')
let subscribeMessage = document.getElementById('subscribe-message')
subscriberForm.addEventListener('submit', function(event){
    let email = document.getElementById('subscribe-email')
    event.preventDefault()
    fetch(`${location.origin}/api/subscriber/`, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscriberForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({"email" : email.value})
    }).then(response => {
        if (response.ok) {
            subscribeMessage.innerHTML = `<h2>Thanks for your subscribing!</h2>`
            console.log('test')
        }
        else {
            alert('Error')
        }
    })
})