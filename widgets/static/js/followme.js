$(document).ready(async function() {
    while(true) {
        await new Promise(r => setTimeout(r, 1000 * 60 * 10))

        // await new Promise(r => setTimeout(r, 1000))

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function(response) {

                $('#followme').html('')

                $('.followme').append(
                    '<b class="followme-text">' + response.text + '</b>'
                )

                $('#followme').removeClass('hidden')

            }
        })

        await new Promise(r => setTimeout(r, 1000 * 45))

        $('#followme').addClass('hidden')
    }
})
