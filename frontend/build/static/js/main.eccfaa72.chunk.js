(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{20:function(e,t,n){},34:function(e,t,n){e.exports=n(64)},39:function(e,t,n){},40:function(e,t,n){},64:function(e,t,n){"use strict";n.r(t);var a=n(0),i=n.n(a),o=n(31),l=n.n(o),r=(n(39),n(2)),s=n(3),c=n(5),m=n(4),u=n(10),d=n(6),p=(n(40),n(20),n(21),function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={selected_item_id:"",sells:[{item:{id:"1",title:"Iphone X",owner:{name_surname:"Furkan Akyol"},item_type:"Phone",description:"\xc7iziksiz s\xfcper ikinci el telefon"},current_price:"10"},{item:{id:"2",title:"Mercedes C Coupe",owner:{name_surname:"Azad Baykara"},item_type:"Car",description:"100.000 kmde doktordan az kullan\u0131lm\u0131\u015f"},current_price:"300.000"}]},n.getData=n.getData.bind(Object(u.a)(n)),n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"componentWillMount",value:function(){this.getData();setInterval(this.getData,1e3)}},{key:"getData",value:function(){var e=this,t=new XMLHttpRequest;t.addEventListener("load",(function(){0==JSON.parse(t.responseText).data.filter((function(t){return e.state.selected_item_id==t.id})).length?e.setState({selected_item_id:"",sells:JSON.parse(t.responseText).data}):e.setState({sells:JSON.parse(t.responseText).data})})),t.open("GET","http://localhost:8000/bid/test/"),t.send()}},{key:"watchItem",value:function(e){var t=new Request("http://localhost:8000/bid/watch-sell/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:this.getCookie("csrftoken"),item_id:e};fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"sendBidReq",value:function(){for(var e=new Request("http://localhost:8000/bid/bidding/1",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=document.getElementById("form-send-bid").children,a=1;a<n.length-1;a++)t[n[a].name]=n[a].value;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"clickHandler",value:function(e){console.log(e),"bid"===e?this.sendBidReq():"fa fa-bell"===e.target.className?(this.watchItem(e.currentTarget.id),console.log("dasdjkas")):this.setState({selected_item_id:e.currentTarget.id})}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"render",value:function(){var e=this;if(""==this.state.selected_item_id)return i.a.createElement("div",null,i.a.createElement("h1",null,"Current Auctions:"),this.state.sells.map((function(t){return i.a.createElement("div",{onClick:function(t){return e.clickHandler(t)},id:t.id,className:"card"},i.a.createElement("div",{className:"additional"},i.a.createElement("div",{className:"item-image"},i.a.createElement("i",{className:"fa fa-bell"}),i.a.createElement("img",{src:"https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg",alt:"Item Photo"}),i.a.createElement("div",{className:"item-price"},t.current_price,"\u20ba"))),i.a.createElement("div",{className:"general"},i.a.createElement("div",{className:"item-info"},i.a.createElement("p",{className:"left"}," Owner: ",t.item.owner.name_surname),i.a.createElement("p",{className:"right"},"Type: ",t.item.item_type)),i.a.createElement("h1",null,t.item.title),i.a.createElement("p",null,t.item.description),i.a.createElement("span",null,"Click On Item to Go Auction Page")))})));var t=this.state.sells.filter((function(t){return t.id==e.state.selected_item_id}))[0],n=this.getCookie("csrftoken");return i.a.createElement("div",null,i.a.createElement("button",{onClick:function(){return e.setState({selected_item_id:""})}},"all items"),i.a.createElement("div",{style:{margin:"50px",border:"1px solid",width:"300px"}},i.a.createElement("p",null,t.item.title),i.a.createElement("p",null,t.item.description),i.a.createElement("p",null,t.item.item_type),i.a.createElement("p",null,t.current_price),i.a.createElement("input",{type:"hidden",name:"csrfmiddlewaretoken",value:n}),i.a.createElement("fieldset",{id:"form-send-bid",className:"form-group"},i.a.createElement("legend",{className:"border-bottom mb-4"},"Make A Bid"),i.a.createElement("input",{type:"text",name:"amount",placeholder:"0"}),i.a.createElement("input",{type:"hidden",name:"item_id",value:t.item.id}),i.a.createElement("button",{className:"btn",onClick:function(){return e.clickHandler("bid")}},"Bid!"))),i.a.createElement("div",{className:"bid_form",id:"login-box"},i.a.createElement("div",{className:"left"},i.a.createElement("h1",null,"Sign up"),i.a.createElement("input",{type:"text",name:"username",placeholder:"Username"}),i.a.createElement("input",{type:"text",name:"email",placeholder:"E-mail"}),i.a.createElement("input",{type:"password",name:"password",placeholder:"Password"}),i.a.createElement("input",{type:"password",name:"password2",placeholder:"Retype password"}),i.a.createElement("input",{type:"submit",name:"signup_submit",value:"Sign me up"})),i.a.createElement("div",{className:"right"},i.a.createElement("span",{className:"loginwith"},"Sign in with",i.a.createElement("br",null),"social network"),i.a.createElement("button",{className:"social-signin facebook"},"Log in with facebook"),i.a.createElement("button",{className:"social-signin twitter"},"Log in with Twitter"),i.a.createElement("button",{className:"social-signin google"},"Log in with Google+")),i.a.createElement("div",{className:"or"},"OR")))}}]),t}(i.a.Component)),h=function(e){function t(e){return Object(r.a)(this,t),Object(c.a)(this,Object(m.a)(t).call(this,e))}return Object(d.a)(t,e),Object(s.a)(t,[{key:"componentWillMount",value:function(){var e=new XMLHttpRequest;e.addEventListener("load",(function(){})),e.open("GET","http://localhost:8000/home/deneme"),e.send()}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"render",value:function(){return i.a.createElement("div",null,i.a.createElement("form",{action:"http://localhost:8000/login/",method:"POST"},i.a.createElement("input",{type:"hidden",name:"csrfmiddlewaretoken",value:this.getCookie("csrftoken")}),i.a.createElement("fieldset",{className:"form-group"},i.a.createElement("legend",{className:"border-bottom mb-4"},"Log In"),i.a.createElement("label",{for:"id_username"},"Username:"),i.a.createElement("input",{type:"text",name:"username",autofocus:"",autocapitalize:"none",autocomplete:"username",maxlength:"150",required:"",id:"id_username"}),i.a.createElement("label",{for:"id_password"},"Password:"),i.a.createElement("input",{type:"password",name:"password",autocomplete:"current-password",required:"",id:"id_password"})),i.a.createElement("div",{className:"form-group"},i.a.createElement("input",{type:"submit",value:"Log In!"}))))}}]),t}(i.a.Component),f=n(12),g=n(13),k=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).clickHandler=n.clickHandler.bind(Object(u.a)(n)),n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"clickHandler",value:function(){var e=new Request("http://localhost:8000/home/add_item/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={title:this.title.value,description:this.description.value,item_type:this.item_type.value,csrfmiddlewaretoken:this.getCookie("csrftoken")};fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){console.log(e)}))}},{key:"render",value:function(){var e=this;return i.a.createElement("div",{className:"bid_form",id:"login-box"},i.a.createElement("div",{className:"center"},i.a.createElement("h1",null,"Add Item"),i.a.createElement("input",{type:"text",ref:function(t){return e.title=t},name:"title",placeholder:"Title"}),i.a.createElement("input",{type:"text",ref:function(t){return e.description=t},name:"description",placeholder:"Description"}),i.a.createElement("input",{type:"text",ref:function(t){return e.item_type=t},name:"item_type",placeholder:"Item type"}),i.a.createElement("button",{className:"submit-button",onClick:this.clickHandler},"Submit")))}}]),t}(i.a.Component),b=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={},n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/profile/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({name_surname:e.data.name_surname,email:e.data.email,balance:e.data.balance})}))}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"render",value:function(){return i.a.createElement("div",null,i.a.createElement("p",null," Ad Soyad: ",this.state.name_surname),i.a.createElement("p",null," Email: ",this.state.email),i.a.createElement("p",null," Bakiye: ",this.state.balance))}}]),t}(i.a.Component),E=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={selected_item_id:"",items:[]},n.toggleDisplay=n.toggleDisplay.bind(Object(u.a)(n)),n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/bid/list-items/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({items:e.data})}))}},{key:"clickHandler",value:function(e){console.log(e.currentTarget.id),this.setState({selected_item_id:e.currentTarget.id})}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"toggleDisplay",value:function(e,t){console.log(t);var n=e.getElementsByClassName(t)[0].style.display;e.getElementsByClassName("instant-increment-form")[0].style.display="none",e.getElementsByClassName("increment-form")[0].style.display="none",e.getElementsByClassName("decrement-form")[0].style.display="none",e.getElementsByClassName(t)[0].style.display="none"==n?"block":"none",e.style.height="none"==n?"decrement-form"==t?"500px":"350px":"200px"}},{key:"clickHandler",value:function(e){console.log(e.target.parentNode.children),this.sendPost(e.target.parentNode)}},{key:"sendPost",value:function(e){for(var t=new Request("http://localhost:8000/bid/sell/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:this.getCookie("csrftoken")},a=e.children,i=0;i<a.length-1;i++)n[a[i].name]=a[i].value;fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"render",value:function(){var e=this;return i.a.createElement("div",null,i.a.createElement("h1",null,"Owned Items"),i.a.createElement("div",{className:"list-wrapper"},this.state.items.map((function(t){return i.a.createElement("div",{id:t.id,className:"card"},i.a.createElement("div",{className:"additional"},i.a.createElement("div",{className:"item-image"},i.a.createElement("img",{src:"https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg",alt:"Item Photo"}))),i.a.createElement("div",{className:"general"},i.a.createElement("div",{className:"item-info"},i.a.createElement("p",{className:"left"}," Owner: ",t.owner.name_surname),i.a.createElement("p",{className:"right"},"Type: ",t.item_type)),i.a.createElement("h1",null,t.title),i.a.createElement("p",null,t.description),i.a.createElement("div",null,i.a.createElement("div",{className:"btn-group"},i.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"decrement-form")}},"Decrement"),i.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"increment-form")}},"Increment"),i.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"instant-increment-form")}},"Instant")),i.a.createElement("div",{className:"form decrement-form",style:{display:"none"}},i.a.createElement("fieldset",{className:"form-group"},i.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),i.a.createElement("input",{type:"text",name:"period",placeholder:"period"}),i.a.createElement("input",{type:"text",name:"delta",placeholder:"delta"}),i.a.createElement("input",{type:"text",name:"stop_decrement",placeholder:"stop decrement"}),i.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),i.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"decrement"}),i.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Decrement"))),i.a.createElement("div",{className:"form increment-form",style:{display:"none"}},i.a.createElement("fieldset",{className:"form-group"},i.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),i.a.createElement("input",{type:"text",name:"instant_sell",placeholder:"instant sell"}),i.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),i.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"increment"}),i.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Increment"))),i.a.createElement("div",{className:"form instant-increment-form",style:{display:"none"}},i.a.createElement("fieldset",{className:"form-group"},i.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),i.a.createElement("input",{type:"text",name:"instant_sell",placeholder:"instant sell"}),i.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),i.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"instant-increment"}),i.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Instant"))))))}))))}}]),t}(i.a.Component),v=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={messages:[]},n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/bid/messages/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({messages:e.data})}))}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"render",value:function(){return i.a.createElement("div",null,this.state.messages.map((function(e){return i.a.createElement("p",null,e)})))}}]),t}(i.a.Component),y=(n(58),function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={route:"",message_count:-1,isMessage:0},n.getCookie=n.getCookie.bind(Object(u.a)(n)),n}return Object(d.a)(t,e),Object(s.a)(t,[{key:"clickHandler",value:function(e){console.log(document.getElementsByClassName("nav-button"));for(var t=document.getElementsByClassName("nav-button"),n=0;n<t.length;n++)t[n].id===e.target.id?t[n].className=t[n].className+" active":t[n].className=t[n].className.split(" ")[0];"message-button"===e.target.id&&this.setState({isMessage:0})}},{key:"socketConnection",value:function(){var e=new WebSocket("ws://localhost:8000/ws/time/");e.onmessage=function(e){var t=JSON.parse(e.data);console.log(t)},e.onclose=function(e){console.error("Chat socket closed unexpectedly")}}},{key:"componentWillMount",value:function(){var e=this;this.socketConnection();setInterval((function(){return e.getMessages(e)}),1e3);console.log("daskhdkjasdjkashdkjashdkjashk")}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var i=n[a].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}return t}},{key:"getMessages",value:function(e){var t=new Request("http://localhost:8000/bid/messages/",{headers:{"X-CSRFToken":e.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:e.getCookie("csrftoken")},a=e;fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(t){if(console.log(t),"Fail"!=t.result){if(-1!=e.state.message_count&&e.state.message_count<t.data.length)return void a.setState({message_count:t.data.length,isMessage:1});a.setState({message_count:t.data.length})}}))}},{key:"render",value:function(){var e=this;return i.a.createElement("div",null,i.a.createElement("link",{href:"https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",rel:"stylesheet"}),i.a.createElement("div",{class:"topnav"}),i.a.createElement(f.a,null,i.a.createElement("div",{class:"topnav"},i.a.createElement(f.b,{className:"nav-button",id:"home-button",onClick:function(t){return e.clickHandler(t)},to:"/bid"},"Home"),i.a.createElement(f.b,{className:"nav-button",id:"add-button",onClick:function(t){return e.clickHandler(t)},to:"/add-item"},"Add Item"),i.a.createElement(f.b,{className:"nav-button",id:"profile-button",onClick:function(t){return e.clickHandler(t)},to:"/profile"},"My Profile"),i.a.createElement(f.b,{className:"nav-button",id:"list-button",onClick:function(t){return e.clickHandler(t)},to:"/list-items"},"List My Items"),i.a.createElement(f.b,{className:"nav-button",id:"message-button",onClick:function(t){return e.clickHandler(t)},to:"/messages"},i.a.createElement("i",{style:{fontSize:"20px",color:this.state.isMessage?"red":"gold"},className:"fa fa-bell"})),i.a.createElement(f.b,{className:"nav-button",id:"logout-button",onClick:function(t){return e.clickHandler(t)},style:{float:"right"},to:"/profile"},"Logout"),i.a.createElement(f.b,{className:"nav-button",id:"admin-button",onClick:function(t){return e.clickHandler(t)},style:{float:"right"},to:"/profile"},"Admin")),i.a.createElement(g.a,{path:"/bid",component:p}),i.a.createElement(g.a,{path:"/login",component:h}),i.a.createElement(g.a,{path:"/add-item",component:k}),i.a.createElement(g.a,{path:"/profile",component:b}),i.a.createElement(g.a,{path:"/list-items",component:E}),i.a.createElement(g.a,{path:"/messages",component:v})))}}]),t}(i.a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(i.a.createElement(y,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[34,1,2]]]);
//# sourceMappingURL=main.eccfaa72.chunk.js.map