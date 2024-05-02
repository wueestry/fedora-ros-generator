# Meta Package
Name:           ros-humble-performance-test-fixture
Version:        0.0.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-performance_test_fixture and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-performance_test_fixture
Requires:       ros2-humble-performance_test_fixture-devel

Obsoletes: ros-humble-performance-test-fixture < 0.0.9-1

%description
Test fixture and CMake macro for using osrf_testing_tools_cpp with
Google Benchmark

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.9-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.9-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.9-1
- Initial humble build
