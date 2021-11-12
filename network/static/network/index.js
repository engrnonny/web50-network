document.addEventListener('DOMContentLoaded', function() {
    var edit_btns = document.querySelectorAll('.post');
    for(var i = 0; i < edit_btns.length; i++){
        edit_btns[i].addEventListener('click', (e) => edit_post(e));
    }        
    document.querySelector('#edited-form').onsubmit = save_post();
});

function edit_post(e) {
    e = window.event;
    let post_id = e.target.id;
    let post_body = document.querySelector(`#body${post_id}`).innerHTML;
    document.querySelector(`#body${post_id}`).innerHTML = `<form method="post" id="edited-form">  
        <div class="form-group">
            <input disabled class="form-control" hidden value="${post_id}" id="edited-post-id">
            <textarea autofocus class="form-control" type="text" name="edited-post" id="edited-post-body">${post_body}</textarea>  
        </div>
        <input class="btn btn-primary" type="submit" value="Post">      
    </form>`
    var posts = document.querySelectorAll('.post');
    for(var i = 0; i < posts.length; i++){
        posts[i].style.display = 'none';
    }
    return false;
}

function save_post() {    
    const body = document.querySelector('#edited-post-body').value;
    const post_id = document.querySelector('#edited-post-id').value;
    fetch(`user/p/edit-post/${post_id}`, {
        method: 'POST',
        body: JSON.stringify({
            body: body
        })
    })
        .then(response => response.json())
            .then(result => {
            if ("message" in result) {
                document.querySelector(`#body${post_id}`).innerHTML = body
                var posts = document.querySelectorAll('.post');
                for(var i = 0; i < posts.length; i++){
                    posts[i].style.display = 'block';
                }
            }
    
            if ("error" in result) {
                // There was an error in sending the email
                // Display the error next to the "To:"
                document.querySelector('#to-text-error-message').innerHTML = result['error']
    
            }
            })
            .catch(error => {
                console.log(error);
            });
    return false;
}
    