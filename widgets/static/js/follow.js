$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function(response) {
                $('#follow-content').html('')

                for (follower of response.followers) {

                    console.log('[DEBUG] follower: ' + follower)

                    $('.follow-body').append(
                        '<span><span class="follower-name">' + follower + '</span> é um bom samaritano!</span>'
                    )
                }
            }
        })
    }, 1000)
})


