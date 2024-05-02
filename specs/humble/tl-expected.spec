# Meta Package
Name:           ros-humble-tl-expected
Version:        1.0.2
Release:        1%{?dist}
License:        Creative Commons Zero v1.0 Universal
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tl_expected and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tl_expected
Requires:       ros2-humble-tl_expected-devel

Obsoletes: ros-humble-tl-expected < 1.0.2-1

%description
C++11/14/17 std::expected with functional-style extensions

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
