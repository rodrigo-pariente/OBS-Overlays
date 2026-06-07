$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function(response) {

                $('#todo-content').html('')

                console.log('[DEBUG] response.todo: ' + response.todo)

                for (const [todo, check] of Object.entries(response.todo)) {
                    // response.todo is not iterable
                    if (check) { 
                        var mark = '✔'
                    } else {
                        var mark = '◉'
                    }

                    $('.todo-body').append(
                        '<span class="mark">' + mark + '</span>' + '<span class="text">' + todo + '</span>'
                    )

                }
            }
        })
    }, 1000)
})
