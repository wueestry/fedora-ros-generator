# Meta Package
Name:           ros-jazzy-gtest-vendor
Version:        1.14.9000
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-gtest_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gtest_vendor
Requires:       ros2-jazzy-gtest_vendor-devel

Obsoletes: ros-jazzy-gtest-vendor < 1.14.9000-1

%description
The package provides GoogleTest.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.14.9000-1
- Update to latest release
