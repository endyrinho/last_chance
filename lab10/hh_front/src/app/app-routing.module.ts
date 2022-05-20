import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CompaniesComponent} from './companies/companies.component';
import {VacanciesComponent} from './vacancies/vacancies.component';


const routes: Routes = [
  { path: '', component: CompaniesComponent},
  { path: 'company/:id', component: VacanciesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
