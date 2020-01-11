import React from 'react';
export default class AddItem extends React.Component { 

    constructor(props){
        super(props);
        this.clickHandler=this.clickHandler.bind(this)
    }

    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = (cookies[i]).trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    clickHandler(){

        var request = new Request(
            'http://localhost:8000/home/add_item/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            title: this.title.value,
            description: this.description.value,
            item_type:this.item_type.value,
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            console.log(response)
        });
    }
    render(){
        return(
            <div className='bid_form' id="login-box">
                <div className='center'>
                <h1>Add Item</h1>
                <input type={"text"} ref={(c) => this.title = c} name={"title"} placeholder={"Title"}></input>
                <input type={"text"} ref={(c) => this.description = c} name={"description"} placeholder={"Description"}></input>
                <input type={"text"} ref={(c) => this.item_type = c} name={"item_type"} placeholder={"Item type"}></input>
                <button className='submit-button'onClick={this.clickHandler}>Submit</button>

                </div>
            </div>




        );
    }
}