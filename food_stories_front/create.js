window.addEventListener('load', async function (event) {
    let response = await fetch('http://localhost:8000/api/categories/')
    let resData = await response.json()
    let categoryList = this.document.getElementById('category-list')
    for (category of resData) {
        categoryList.innerHTML += `
        <option value="${category.id}">${category.title}</option>
        `
    }
    let responseTags = await this.fetch('http://localhost:8000/api/tags/')
    let resDataTags = await responseTags.json()
    let tagList = this.document.getElementById('tag-list')
    for (tag of resDataTags) {
        tagList.innerHTML += `
        <option value="${tag.id}">${tag.title}</option>
        `
    }
})

let token = localStorage.getItem('token')

let creationForm = document.getElementById('creation-form')
creationForm.addEventListener('submit', function (event) {
    event.preventDefault()
    let formData = new FormData(creationForm)
    fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    })
})