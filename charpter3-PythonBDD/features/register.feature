#coding=utf-8
Feature: Register User

    As a developer
    This is my first bdd project
    Scenario: open register website
        When I open the register website "https://www.incnjp.com/member.php?mod=jionxc"
        Then I expect that the title is "注册"

    Scenario: input username
        When I set with useremail "919824370qq.com"
        And I set with username "z1069867141"
        And I set with password "z54821348123"
        And I set with code "test"
        And I click with registerbutton
        Then I expect that text "验证码错误"