import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TestcategoryComponent } from './testcategory.component';

describe('TestcategoryComponent', () => {
  let component: TestcategoryComponent;
  let fixture: ComponentFixture<TestcategoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TestcategoryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TestcategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
