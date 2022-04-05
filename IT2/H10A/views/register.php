<?php
    session_start();
    if(isset($_POST["register"]) )
    {
        if($_POST["pwd"] == $_POST["pwd_check"])
        {
            /* Vytvoreni asociativniho pole a nasledne ulozeni do cokiny */
            $user=array("Jmeno"=>$_POST['name'],"Email"=>$_POST['email'],"PWD"=>$_POST['pwd']);
            setcookie("User", serialize($user), time()+3600, "/");
            header("Location: ../index.php");
        }
        else{
            $_SESSION['errMess']="Hesla se neshoduji.";
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
            .loginPage{
                font-size: 16px;
                color:black;
                text-decoration: none;
            }
            .loginPage:hover{
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
            <h1> Registrační formulář </h1>
            <?php
                if(isset($_SESSION['errMess']))
                {
                    echo "<p style='color:red;text-align:center'>".$_SESSION['errMess']." </p>";
                    unset($_SESSION['errMess']);
                }
            ?>
            <div class=formular>
                <form class="loginform" method="POST" action="">
                    <label for="name">Přihlašovací jméno</label><br>
                    <input type="text" name="name" id="login" required><br>
                    <label for="name">Email</label><br>
                    <input type="email" name="email" id="email" required><br>
                    <label for="pws">Heslo</label><br>
                    <input type="password" name="pwd" id="pwd" required><br>
                    <label for="pwd_check">Heslo pro kontrolu</label><br>
                    <input type="password" name="pwd_check" id="pwd_check" required><br>
                    <input type="submit" value="Registrovat se" name="register"><br>
                    <a class="loginPage"  href="../index.php">Přihlásit se</a>
                </form>
            </div>
    </body>
</html>