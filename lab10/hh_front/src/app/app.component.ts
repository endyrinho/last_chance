import { Component, OnInit } from '@angular/core';
import { CompanyService } from './company.service';
import { CompanyService } from '..';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implement OnInit {
  title = 'hh_front';

  logged = false;

  username = '';
  password = '';

  constructor(private companyService: CompanyService)

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  login() {
    this.CompanyService.login(this.username, this.password)
    .subscribe(res => {

      localStorage.setItem('token', res.token);

      this.logged = true;

      this.username = '';
      this.password = '';

    });
  }
  logout() {
    localStorage.clear();
    this.logged = false;
  }
}
