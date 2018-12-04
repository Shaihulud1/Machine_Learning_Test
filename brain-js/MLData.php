<?php
if(isset($_POST['action']))
{
    switch ($_POST['action']) {
        case 'set':
            $data = $_POST['mlData'];
            if(!$data) die();
            $file = isset($_POST['save']) ? trim(htmlspecialchars($_POST['file'])) : 'resultJson';
            file_put_contents($file.'.json', $data);
        break;

        case 'get':
            $file = isset($_POST['save']) ? trim(htmlspecialchars($_POST['file'])) : 'resultJson';
            $mlData = file_get_contents($file.'.json');
            print_r($mlData);
        break;
    }

}
