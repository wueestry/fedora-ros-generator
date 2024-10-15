# Meta Package
Name:           ros-humble-perception
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-perception and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-perception
Requires:       ros2-humble-perception-devel

Obsoletes: ros-humble-perception < 0.10.0-1

%description
A package which aggregates common perception packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Update to latest release
