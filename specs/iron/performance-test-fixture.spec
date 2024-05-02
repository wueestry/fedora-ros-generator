# Meta Package
Name:           ros-iron-performance-test-fixture
Version:        0.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-performance_test_fixture and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-performance_test_fixture
Requires:       ros2-iron-performance_test_fixture-devel

Obsoletes: ros-iron-performance-test-fixture < 0.1.1-1

%description
Test fixture and CMake macro for using osrf_testing_tools_cpp with
Google Benchmark

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.1.1-1
- Update to latest release
