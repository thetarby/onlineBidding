import React from 'react';
import './App.css';
import Bid from './routes/Bid'
import Login from './routes/login'
import {BrowserRouter as Router, Route} from 'react-router-dom'
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
		}
        //this.handleLogin = this.handleLogin.bind(this);
	}

    clickHandler(e){
        console.log(document.getElementsByClassName("topnav")[0].getElementsByTagName("a"))

        var buttons=document.getElementsByClassName("topnav")[0].getElementsByTagName("a");
        for(var i=0; i<buttons.length; i++){
            if(buttons[i].id===e.target.id) buttons[i].className="active"
            else buttons[i].className=""
        }
    }

    render(){
        
        return (
            <div>
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
                <div class="topnav">
                        <a id={"home-button"} onClick={(e)=>this.clickHandler(e)} href={'./bid'}>Home</a>
                        <a id={"auction-button"} onClick={(e)=>this.clickHandler(e)} href={'./bid'}>View Auction Page</a>
                        <a id={"add-item-button"} onClick={(e)=>this.clickHandler(e)} href={'./add-item'} >Add item</a>
                        <a id={"profile-button"} onClick={(e)=>this.clickHandler(e)} href={'./profile'}>My Profile</a>
                        <a id={"list-items-button"} onClick={(e)=>this.clickHandler(e)} href={'./list-items'}>List My Items</a>
                        <a id={"messages-button"} onClick={(e)=>this.clickHandler(e)} href={'./messages'} ><i style={{fontSize:"20px", color:"gold"}} className={"fa fa-bell"}></i></a>
                        <a id={"logout-button"} style={{float:"right"}}onClick={(e)=>this.clickHandler(e)} >Logout</a>,
                        <a id={"admin-button"} style={{float:"right"}} onClick={(e)=>this.clickHandler(e)}>Admin</a>
                </div>
        
            
                <Router>
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
