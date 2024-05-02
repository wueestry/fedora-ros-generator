# Meta Package
Name:           ros-iron-tlsf
Version:        0.8.2
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tlsf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tlsf
Requires:       ros2-iron-tlsf-devel

Obsoletes: ros-iron-tlsf < 0.8.2-1

%description
TLSF allocator version 2.4.6

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.8.2-1
- Update to latest release
