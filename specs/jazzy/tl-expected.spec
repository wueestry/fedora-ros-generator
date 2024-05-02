# Meta Package
Name:           ros-jazzy-tl-expected
Version:        1.0.2
Release:        1%{?dist}
License:        Creative Commons Zero v1.0 Universal
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tl_expected and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tl_expected
Requires:       ros2-jazzy-tl_expected-devel

Obsoletes: ros-jazzy-tl-expected < 1.0.2-1

%description
C++11/14/17 std::expected with functional-style extensions

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
