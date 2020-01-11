import React from 'react';
export default class Login extends React.Component { 
    constructor(props){
        super(props)
    }
    componentWillMount(){
        var xhr = new XMLHttpRequest()

        // get a callback when the server responds
        xhr.addEventListener('load', () => {
            // update the state of the component with the result here
            
        })
        // open the request with the verb and the url
        xhr.open('GET', 'http://localhost:8000/home/deneme')
        // send the request
        xhr.send()
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
                <form action={"http://localhost:8000/login/"} method={"POST"}>
                <input type={"hidden"} name={"csrfmiddlewaretoken"} value={this.getCookie('csrftoken')}></input>
                <fieldset className={"form-group"}>
                    <legend className={"border-bottom mb-4"}>Log In</legend>
                    <label for={"id_username"}>Username:</label><input type={"text"} name={"username"} autofocus={""} autocapitalize={"none"} autocomplete={"username"} maxlength={"150"} required={""} id={"id_username"}></input>
                    <label for={"id_password"}>Password:</label><input type={"password"} name={"password"} autocomplete={"current-password"} required={""} id={"id_password"}></input>
                </fieldset>
                <div className={"form-group"}>
                    <input type={"submit"} value={"Log In!"}></input>
                </div>
                </form>
            </div>
			);
	}
}