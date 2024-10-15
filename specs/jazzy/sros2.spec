# Meta Package
Name:           ros-jazzy-sros2
Version:        0.13.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sros2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sros2
Requires:       ros2-jazzy-sros2-devel

Obsoletes: ros-jazzy-sros2 < 0.13.2-1

%description
Command line tools for managing SROS2 keys

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.0-1
- Update to latest release
