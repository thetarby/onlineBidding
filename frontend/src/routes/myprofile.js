import React from 'react';
export default class MyProfile extends React.Component { 
    constructor(props){
        super(props)
        this.state = {}
        this.watchItemType=this.watchItemType.bind(this)
    }
    componentWillMount(){
        var request = new Request(
            'http://localhost:8000/profile/',
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
                    "name_surname": json.data.name_surname, 
                    "email": json.data.email,
                    "balance": json.data.balance
            })
        })



        var request = new Request(
            'http://localhost:8000/bid/user-history',
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
            
        })
    }
    watchItemType(){
        var request = new Request(
            'http://localhost:8000/bid/watch-item-type/'+document.getElementById('item-type-watch').value
        );
        var thisOfClass=this;
        fetch(request, {
            method: 'GET',
        }).then(function(response) {
            return (response.json())
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
                <p> Ad Soyad: { this.state.name_surname }</p>
                <p> Email: { this.state.email }</p>
                <p> Bakiye: { this.state.balance }</p>

                <input type={"text"} name={"item_type"} placeholder={"item type to watch"} id={'item-type-watch'}></input>
                <button onClick={this.watchItemType}>Submit</button>
            </div>
			);
	}
}