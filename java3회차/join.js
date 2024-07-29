const form = document.getElementById("form")

form.addEventListener("submit", function(event){
  event.preventDefault()

  let userid = event.target.id.value
  let userpw1 = event.target.pw1.value
  let userpw2 = event.target.pw2.value
  let username = event.target.name.value
  let userphone = event.target.phone.value
  let userposition = event.target.position.value
  let usergender = event.target.gender.value
  let useremail = event.target.email.value
  let userintro = event.target.intro.value
  
  if(userid.length < 4){
    alert("아이디가 너무 짧습니다. 4자 이상 입력해주세요.")
    return
  }
  if(userpw1 !== userpw2){
    alert("비밀번호가 일치하지 않습니다.")
    return
  }
  document.body.innerHTML = ""
  document.write(`<p>회원 가입 시 입력한 내역은 다음과 같습니다.</p>`)
  document.write(`<p>아이디 ${userid}</P>`)
  document.write(`<p>이름 ${username}<P>`)
  document.write(`<p>전화번호${userphone}</P>`)
  document.write(`<p>원하는 직무${userposition}</P>`)



})