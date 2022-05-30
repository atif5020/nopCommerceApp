# step 1. Create new project & install all required packages/plugins
            # 1. Selenium
            # 2. pytest --->for unittest framework
            # 3.pytest-html  --->to generate html reports
            # 4.pytest-xdist  -->runs parallel testing
            # 5.openpyxl
            # 6.allure-pytest  --> (optional) --> to generate allure reports

# step 2. Create folder structure
            # 1. pageObjects (package)
            # 2. testCases (package)
            # 3.utilities (package)
            # 4. TestData (folder)
            # 5.Configuations (folder)
            # 6.Logs (folder)
            # 7.Screenshots (folder)
            # 8.Reports (folder)

# step 3. automate 1st test case: Login testcase
            # 1. create LoginPage Object Class under 'pageObjects'
            # 2.create LoginTest under 'testCases'
            # 3.create conftest.py under 'testCases' -->to avoid duplicate code

# step 4. Capture screenshots on failure

# step 5. Read common values fom ini file
            # 1. add 'config.ini' file in configuration folder
            # 2. create 'readProperties.py' utility file under utilites package to read common data
            # 3. replace hard coded values in 'Login testcase'

# step 6. adding logs to test cases
            # 1. add customLogger.py under utilities package
            # 2. add logs to Login Test case

# step 7. Run tests on desired browser/Cross Browser/Parallel
            # 1. update conftest.py with required fixture
            # 2. pass browsername as argument in command line

            # command to run on desired browser:
                    # -->  pytest -v -s pathOfTestCase --browser chrome
                    # '->  pytest -v -s testCases/test_login.py --browser chrome
                    #-->  pytest -v -s pathOfTestCase --browser firefox
            # command to run tests Parallel:
                    # 1st install package --> pytest-xdist
                         # --> pytest -v -s -n=3 pathOfTestCase --browser chrome
                    # -n=3 means maximum 3 tests in a test case will run parallel

# step 8. Generate Html reports
            # 1. update confest.py withpytest hooks
            # 2. run below command to generate html report
                     # command --> pytest -v -s -n=2 --html=Reports\report.html testCases/test_login.py
                             # '-> Reports\report.html is path where to save and with what name

# step 9.  Automating data-driven test case
            # 1. prepate test data in excel sheet and place it in TestData folder
            # 2. create ExcelUtils.py utility class under utilities package
            # 3. Create LoginDataDrivenTest under TestCases

# step 10. adding new test cases
            # 1. add new customer
            # 2. search custome by email
            # 3. search customer by name

# step 11.  Grouping tests
            # 1. grouping markers(add markers to every test method)
                    # @pytest.mark.sanity
                    # @pytest.mark.regression
            # 2. add marker eneries in pytest.ini file
                    # [pytest]
                    # markers =
                                # sanity
                                # regression
            # 3. execute in terminal
                    # pytest -v -s -m "sanity" testCases/(-->this is folder name)
                    # pytest -v -s -m "sanity and regression" testCases/ -->tests which are both sanity and regression runs
                    # pytest -v -s -m "sanity or regression" testCases/  -->tests which either sanity or regression, runs
                    # pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

# step 12. # Run tests in command prompt(outside selenium) and run.bat file
            # create run.bat file -->(at project location in file explorer) create new text file and save it as 'run.bat'
            # then edit this file and paste/type all commands which to run ,
            # then comment all other commands other than one which to run
            # to comment before command type 'rem'
            # to run command just open run.bat file

# step 13. Push the code to the Git and GitHub repository
            # 1. create local git repository for your project
                    # 1. go to your project location , click bash here in right click which will open shell/git command
                    # 2. in git shell type-->  git init ->this will create empty local repository
            # 2.  connect local git repository with github remote repository
                    # 1. create new repository (if not already created) in GitHub with project name and copy url
                        # https://github.com/atif5020/nopCommerceApp.git
                    # 2. git command to connect
                        # git remote add origin https://github.com/atif5020/nopCommerceApp.git
            # 3. before doing commit code to git repository, very first time run these two commands ...only once
                    # git config --global user.name "atif5020"
                    # git config --global user.email "aatifray5020@gmail.com"
            # 4. to check file status (commited/not commit)
                    # git status
            # 5. add files to staging area before commiting to git
                    # git add -A
            # 6.

