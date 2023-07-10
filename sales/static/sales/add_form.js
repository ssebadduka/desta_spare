// let 
let formSet = document.querySelector('.formset')
let addBtn = document.querySelector('#add-more')
let removeBtn = document.querySelector('#remove')
let totalForms = document.querySelector('#id_form-TOTAL_FORMS')
let count = 1

addBtn.addEventListener('click', addForm)

function addForm(e) {
    e.preventDefault()
    let formRow = document.querySelectorAll('.form-row')
    let formNum = formRow.length - 1
    count++

    let newForm = formRow[0].cloneNode(true) 
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum++ 
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    formSet.insertBefore(newForm, addBtn)

    totalForms.setAttribute('value', `${formNum+1}`)
}

removeBtn.addEventListener('click', removeForm)

function removeForm(e) {
    e.preventDefault()

    if (count > 1) {
        let allFormsets = document.getElementsByClassName('form-row')
        let totalLength = allFormsets.length

        allFormsets[totalLength - 1].remove()

        totalForms.setAttribute('value', `${totalLength-1}`)
        count--
    }
    else {
        alert('Not allowed')
    }
}
