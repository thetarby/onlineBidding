import React from 'react';
export default class Messages extends React.Component { 
    constructor(props){
        super(props)
        this.state = {messages:[]}
    }
    componentWillMount(){
        var request = new Request(
            'http://localhost:8000/bid/messages/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            console.log(json)
            thisOfClass.setState(
                {
                    messages:json.data
            })
        })
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
	render(){
		return(
			<div>
                {
                    this.state.messages.map((message)=>
                        <p>{message}</p>
                    )
                }
            </div>
			);
	}
}