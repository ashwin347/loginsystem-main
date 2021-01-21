function send(){
            
    username=document.getElementById('username').value
    password=document.getElementById('password').value
    
    if(username=="" || password==""){
        return 
    }
    window.location.href='/signup?username='+username+"&password="+password;
}
function edit(id){
    event.preventDefault();
    document.getElementById('edit_username').style.display="None"
    document.getElementById('update_username').style.display="block"
    
    /*element=document.getElementById('username')
    input=document.createElement('input')
    input.value='{{user.name}}'
    element.innerHTML=""
    element.appendChild(input)*/
}
function update(field){
    new_value=input.value
    //window.location.href='update_profile?type='+field+'&newdata='+new_value+'&email='+user.email;
    
}
function back(){
    window.location.href='admin'
}