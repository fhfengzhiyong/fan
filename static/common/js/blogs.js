/**
 * Created by xiaowu on 2015/12/15.
 */
function praise(id) {
    $.ajax({
        url: '/blogs/praise',
        data: {
            id: id
        },
        dataType: 'json',
        type: 'POST',
        success: function (data) {
            $("#" + id).html(data.praise)

        }
    })
}

