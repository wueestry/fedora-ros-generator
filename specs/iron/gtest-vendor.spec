# Meta Package
Name:           ros-iron-gtest-vendor
Version:        1.10.9005
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-gtest_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gtest_vendor
Requires:       ros2-iron-gtest_vendor-devel

Obsoletes: ros-iron-gtest-vendor < 1.10.9005-1

%description
The package provides GoogleTest.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.10.9005-1
- Update to latest release
