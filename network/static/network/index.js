document.addEventListener('DOMContentLoaded', function() {
    var edit_btns = document.querySelectorAll('.post');
    for(var i = 0; i < edit_btns.length; i++){
        edit_btns[i].addEventListener('click', (e) => edit_post(e));
    }   
    var like_btns = document.querySelectorAll('.like');
    for(var i = 0; i < like_btns.length; i++){
        like_btns[i].addEventListener('click', (e) => like_post(e));
    }        
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
        <input class="btn btn-primary" id="submit" type="submit" value="Post">     
        <span><button class="btn btn-primary" id="cancel">cancel</button></span>     
    </form>`
    var posts = document.querySelectorAll('.post');
    for(var i = 0; i < posts.length; i++){
        posts[i].style.display = 'none';
    }
    document.querySelector('#submit').addEventListener('click', save_post);
    document.querySelector('#cancel').addEventListener('click', cancel(`${post_body}, ${post_id}`));
}

function like_post(e) {
    e = window.event;
    let target_id = e.target.id
    let post_id = document.querySelector(`#${target_id}-hidden`).innerHTML.trim();
    console.log(post_id);
    
    fetch(`/user/p/l/${post_id}`, {
        method: "POST",
        body: JSON.stringify({
            post_id: post_id
        })
    })
        .then(response => response.json())
            .then(result => {
            if ("message" in result) {
                console.log(result)
                console.log(e.target.innerHTML)
                if (e.target.innerHTML == "Unlike") {
                    e.target.innerHTML = "Like"
                }
                else if (e.target.innerHTML == "Like") {
                    e.target.innerHTML = "Unlike"
                }
            }
    
            if ("error" in result) {
                document.querySelector('#to-text-error-message').innerHTML = result['error']
    
            }
            })
            .catch(error => {
                console.log(error);
            });
}

function cancel(post_body, post_id) {
    document.querySelector(`#body${post_id}`).innerHTML = post_body
    var posts = document.querySelectorAll('.post');
    for(var i = 0; i < posts.length; i++){
        posts[i].style.display = 'block';
    }
}

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

function save_post() {    
    const body = document.querySelector('#edited-post-body').value;
    console.log(body)
    const post_id = document.querySelector('#edited-post-id').value;
    console.log(post_id)
    // const csrftoken = getCookie('csrftoken');
    // const request = new Request(
    //     `user/p/edit-post/${post_id}`,
    //     {headers: {'X-CSRFToken': csrftoken}}
    // );
    fetch(`/user/p/edit-post/${post_id}`, {
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
                document.querySelector('#to-text-error-message').innerHTML = result['error']
    
            }
            })
            .catch(error => {
                console.log(error);
            });
    return false;
}
    