# Meta Package
Name:           ros-jazzy-launch-xml
Version:        3.4.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch_xml and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch_xml
Requires:       ros2-jazzy-launch_xml-devel

Obsoletes: ros-jazzy-launch-xml < 3.4.2-1

%description
XML frontend for the launch package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.2-1
- Update to latest release
