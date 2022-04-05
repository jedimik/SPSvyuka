<?php
session_start();
if(isset($_SESSION['logged']) && $_SESSION['logged']==true)
{
    header('Location: views/page1.php');
}

if(isset($_POST['login']))
{
    if(isset($_COOKIE['User']))
    {
        $user=unserialize($_COOKIE['User']);       
        if($user['Jmeno']==$_POST['name'] && $user['PWD']==$_POST['pwd'])
        {
            $_SESSION['logged']=true;
            $_SESSION['loggedUser']=$user['Jmeno'];
            header("Location: views/page1.php");
        }   
    }
    else{
        $_SESSION['errMess']="Zadny uzivatel neni registrovan.";
    }
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Dnesni formularova hodina</title>
        <style>
            body{
                background-color: #85fa78;
            }
            h1{
                text-align: center;
            }
            .registerPage{
                font-size: 16px;
                color:black;
                text-decoration: none;
            }
            .registerPage:hover{
                color:blue;
            }
            .formular{
                display:block;
                position:relative;
                margin-left: auto;
                margin-right: auto;
            }
            .loginform{
                position:absolute;
                left: 50%;
                margin-right: -50%;
                transform: translate(-50%, 0%);
                border: 1px solid black;
                text-align: center;
            }
        </style>
    </head>
    <body>
    <?php
    if(isset($_SESSION['errMess']))
    {
        echo "<p style='color:red;text-align:center'>".$_SESSION['errMess']." </p>";
        unset($_SESSION['errMess']);
    }
    ?>
            <h1> Přilašovací formulář </h1>
            <div class=formular>
                <form class="loginform" method="POST" action="">
                    <label for="name">Přihlašovací jméno</label><br>
                    <input type="text" name="name" id="name" required><br>
                    <label for="pws">Heslo</label><br>
                    <input type="password" name="pwd" id="pwd" required><br>
                    <input type="submit" value="Přihlásit se" name="login"><br>
                    <a class="registerPage"  href="views/register.php">Registrovat se</a>
                </form>
            </div>
    </body>
</html>