<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Base extends CI_Controller {

public function index()
	{
		$this->load->view('includes/header.php');
		$this->load->view('includes/ukravtodor.php');
		$this->load->view('includes/side_menu.php');
		$this->load->view('includes/footer.php');
	}
}
