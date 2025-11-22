const signupForm = document.getElementById("signupForm") 
const loginForm = document.getElementById("loginForm")
const signupName = document.getElementById("signupName")
const signupEmail = document.getElementById("signupEmail")
const signupPassword = document.getElementById("signupPassword")
const loginEmail = document.getElementById("loginEmail")
const loginPassword = document.getElementById("loginPassword")
const createMessageForm = document.getElementById("createMessageForm")
const messageInput = document.getElementById("message")
const messageBar = document.getElementById("message_bar")
const deleteForm = document.querySelectorAll(".deleteForm")

if (signupForm){
    signupForm.addEventListener("submit", async function(event) {
        event.preventDefault();
            if(signupName.value === ""){
            alert("請輸入註冊姓名")
        }
        else if(signupEmail.value === ""){
            alert("請輸入註冊電子信箱")
        }
        else if(signupPassword.value === ""){
            alert("請輸入註冊密碼")
        }
        else{
        const res = await fetch("/signup", {
            method: "POST",
            body: new FormData(signupForm)
        });
        const data = await res.json();
        if (data.status === "ok") {
            alert(data.msg);
            signupForm.querySelectorAll("input").forEach(input => input.value = "");    } else {
            window.location.href = `/ohoh?msg=${encodeURIComponent(data.msg)}`;
        }
        }
    });
}
if(loginForm){
    loginForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        if(loginEmail.value === "" || loginPassword.value === ""){
            alert("請輸入登入信箱或密碼");
            return;}
        
        const res = await fetch("/login", {
            method: "POST",
            body: new FormData(loginForm)
        });
        const data = await res.json();
        if (data.status === "error") {
        window.location.href = `/ohoh?msg=${encodeURIComponent(data.msg)}`;
        return;
        }else if (data.status === "ok"){
        window.location.href = "/member";
        }
            
    });
}
if(createMessageForm){
    createMessageForm.addEventListener("submit", async function(event) {
        if(messageInput.value === ""){
        alert("請輸入留言內容");
        event.preventDefault();
        return;}
        });
}

if(deleteForm){
    deleteForm.forEach(form => {
    form.addEventListener("submit", function(event) {
        if (!confirm("確定要刪除這則留言嗎？")) {
            event.preventDefault(); 
        }
    });
    });
}

