import React from 'react';
import './App.css';
import Bid from './routes/Bid'
import Login from './routes/login'

import {BrowserRouter as Router, Route} from 'react-router-dom'
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
                <div class="topnav">
                        <a id={"home-button"} onClick={(e)=>this.clickHandler(e)} href={'./bid'}>Home</a>
                        <a id={"auction-button"} onClick={(e)=>this.clickHandler(e)}>View Auction Page</a>
                        <a id={"add-item-button"} onClick={(e)=>this.clickHandler(e)}>Add item</a>
                        <a id={"profile-button"} onClick={(e)=>this.clickHandler(e)}>My Profile</a>
                        <a id={"list-items-button"} onClick={(e)=>this.clickHandler(e)}>List My Items</a>
                        <a id={"messages-button"} onClick={(e)=>this.clickHandler(e)}><i style={{fontSize:"20px"}} className={"fa fa-bell"}></i></a>
                        <a id={"logout-button"} style={{float:"right"}}onClick={(e)=>this.clickHandler(e)} >Logout</a>,
                        <a id={"admin-button"} style={{float:"right"}} onClick={(e)=>this.clickHandler(e)}>Admin</a>
                </div>
        
            
                <Router>
                    <Route path = "/bid" component ={Bid}></Route>
                    <Route path = "/login" component ={Login}></Route>
                </Router>
            </div>
        );
    }
}
export default App;
