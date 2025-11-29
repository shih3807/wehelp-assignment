const signupForm = document.getElementById("signupForm"); 
const loginForm = document.getElementById("loginForm");
const signupName = document.getElementById("signupName");
const signupEmail = document.getElementById("signupEmail");
const signupPassword = document.getElementById("signupPassword");
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");
const searchIdInput = document.getElementById("search_id");
const searchBtn = document.getElementById("search_btn");
const resultDiv = document.getElementById("search_result");
const updateNameInput = document.getElementById("update_name");
const updateNameBtn = document.getElementById("update_name_btn");
const updateNameDiv = document.getElementById("update_name_result");
const welcomeText = document.getElementById("welcome-text");
const memberQueryBtn = document.getElementById("member-query_btn");
const memberQueryDiv = document.getElementById("member-query_result");

if (signupForm){
    signupForm.addEventListener("submit", async (event) => {
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
    loginForm.addEventListener("submit", async (event)=> {
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

if(searchBtn){
    searchBtn.addEventListener("click", async ()=> {
        const id = searchIdInput.value;
        if(id === ""){
            alert("請輸入欲查詢的會員編號");
            return;
        }
        
        if (!/^[1-9]\d*$/.test(id)) {
            alert("請輸入正整數");
            return;
        }

        const res = await fetch(`/api/member/${id}`);
        const data = await res.json();

        if (data.data === null) {
            resultDiv.textContent = "No Data";
        } else {
            resultDiv.textContent = `${data.data.name}(${data.data.email})`;
        }
        });
    }

if (updateNameBtn) {
    updateNameBtn.addEventListener("click", async () => {
        const newName = updateNameInput.value;
        if (newName === "") {
            alert("請輸入新的姓名");
            return;
        }
        
        const res = await fetch("/api/member", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: newName })
        });
        const data = await res.json();

        if (data.ok) {
            updateNameDiv.textContent = "更新成功";
            welcomeText.textContent = `${newName}，歡迎登入系統`;
        } else {
            updateNameDiv.textContent = "更新失敗";
        }
        
    });
}

if (memberQueryBtn) {
    memberQueryBtn.addEventListener("click", async () => {
                
        const res = await fetch("/api/member-query");
        const data = await res.json();

        memberQueryDiv.innerHTML = "";
        if (data.data.length === 0) {
            memberQueryDiv.textContent = "無查詢紀錄";
        } else {
            data.data.forEach(item => {
            const p = document.createElement("p");
            p.textContent = `${item.name} ( ${item.time})`;
            memberQueryDiv.appendChild(p);
            });
        }
    });
}     

