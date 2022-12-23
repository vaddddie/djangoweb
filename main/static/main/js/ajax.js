$("#form_id").on("submit", function() {

    let dataForm = $(this).serialize()

    $.ajax({
        url: '{% url 'management' %}',
        method: 'post',
        dataType: 'html',
        data: dataForm,
    });
})
