# Meta Package
Name:           ros-iron-sros2
Version:        0.11.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-sros2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-sros2
Requires:       ros2-iron-sros2-devel

Obsoletes: ros-iron-sros2 < 0.11.3-1

%description
Command line tools for managing SROS2 keys

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.11.3-1
- Update to latest release
