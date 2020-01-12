import React from 'react';
import './App.css';
import Bid from './routes/Bid'
import Login from './routes/login'
import {BrowserRouter as Router, Route, Redirect,Link} from 'react-router-dom'
import AddItem from './routes/addItem';
import MyProfile from './routes/myprofile';
import ListItems from './routes/listItems';
import Messages from './routes/messages';

import'bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component {
    constructor(props){
		super(props);
		this.state={
            route:'',
            message_count:-1,
            isMessage:0
		}
        //this.handleLogin = this.handleLogin.bind(this);
        this.getCookie=this.getCookie.bind(this)
	}

    clickHandler(e){
        console.log(document.getElementsByClassName("nav-button"))

        var buttons=document.getElementsByClassName("nav-button");
        for(var i=0; i<buttons.length; i++){
            if(buttons[i].id===e.target.id) buttons[i].className=buttons[i].className+" active"
            else buttons[i].className=buttons[i].className.split(' ')[0]

        }

        if(e.target.id==='message-button') this.setState({isMessage:0})
    }


    socketConnection(){
        var roomName = "{{ room_name|escapejs }}";

        var chatSocket = new WebSocket(
            'ws://localhost:8000'+
            '/ws/time/');
    
        chatSocket.onmessage = function(e) {
            var data = JSON.parse(e.data);
            console.log(data)
        };
    
        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    

    }
    componentWillMount(){
        this.socketConnection()
        let counter = setInterval(()=>this.getMessages(this), 1000);
        console.log('daskhdkjasdjkashdkjashdkjashk')

    }
    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    getMessages(this_) {
        var request = new Request(
            'http://localhost:8000/bid/messages/',
            {headers: {'X-CSRFToken': this_.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this_.getCookie('csrftoken')
        };
        var thisOfClass=this_;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            console.log(json)
            if(json.result!='Fail'){
                if(this_.state.message_count!=-1 && this_.state.message_count<json.data.length){
                    thisOfClass.setState(
                        {
                            message_count:json.data.length,
                            isMessage:1
                    })
                    return
                }
                thisOfClass.setState(
                    {
                        message_count:json.data.length,
                })
            }
        })
    }
    render(){
        
        return (
            <div>
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />

                <div class="topnav">
 
                </div>

            
                <Router>
                    <div class="topnav">
                        <Link className={'nav-button'} id={"home-button"} onClick={(e)=>this.clickHandler(e)} to="/bid">Home</Link>
                        <Link className={'nav-button'} id={"add-button"} onClick={(e)=>this.clickHandler(e)} to="/add-item">Add Item</Link>
                        <Link className={'nav-button'} id={"profile-button"} onClick={(e)=>this.clickHandler(e)} to="/profile">My Profile</Link>
                        <Link className={'nav-button'} id={"list-button"} onClick={(e)=>this.clickHandler(e)} to="/list-items">List My Items</Link>
                        <Link className={'nav-button'} id={"message-button"} onClick={(e)=>this.clickHandler(e)} to="/messages"><i style={{fontSize:"20px", color:this.state.isMessage ? "red":"gold"}} className={"fa fa-bell"}></i></Link>

                        <a className={'nav-button'} id={"logout-button"} href='/logout' style={{float:"right"}}>Logout</a>
                        <Link className={'nav-button'} id={"admin-button"} onClick={(e)=>this.clickHandler(e)} style={{float:"right"}} to="/profile">Admin</Link>
                    </div>
                    <Route path = "/bid" component ={Bid}></Route>
                    <Route path = "/login" component ={Login}></Route>
                    <Route path = "/add-item" component ={AddItem}></Route>
                    <Route path = "/profile" component ={MyProfile}></Route>
                    <Route path = "/list-items" component ={ListItems}></Route>
                    <Route path = "/messages" component ={Messages}></Route>

                </Router>
            </div>
        );
    }
}
export default App;
