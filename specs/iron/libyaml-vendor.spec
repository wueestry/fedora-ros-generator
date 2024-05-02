# Meta Package
Name:           ros-iron-libyaml-vendor
Version:        1.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/yaml/libyaml
Summary:        Meta package for ros2-iron-libyaml_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-libyaml_vendor
Requires:       ros2-iron-libyaml_vendor-devel

Obsoletes: ros-iron-libyaml-vendor < 1.5.0-1

%description
Vendored version of libyaml.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.5.0-1
- Update to latest release
